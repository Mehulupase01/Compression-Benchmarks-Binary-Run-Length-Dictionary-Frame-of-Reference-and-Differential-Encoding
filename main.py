import subprocess
import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

data_files = {
    "int8": ["l_discount-int8.csv", "l_linenumber-int8.csv", "l_quantity-int8.csv", "l_tax-int8.csv"],
    "int16": ["l_discount-int16.csv", "l_linenumber-int16.csv", "l_quantity-int16.csv", "l_tax-int16.csv", "l_suppkey-int16.csv"],
    "int32": ["l_discount-int32.csv", "l_linenumber-int32.csv", "l_orderkey-int32.csv", "l_partkey-int32.csv", "l_quantity-int32.csv", "l_suppkey-int32.csv", "l_orderkey-int32.csv", "l_partkey-int32.csv", "l_tax-int32.csv", "l_extendedprice-int32.csv"],
    "int64": ["l_discount-int64.csv", "l_linenumber-int64.csv", "l_orderkey-int64.csv", "l_partkey-int64.csv", "l_quantity-int64.csv", "l_suppkey-int64.csv", "l_orderkey-int64.csv", "l_partkey-int64.csv", "l_tax-int64.csv", "l_extendedprice-int64.csv"],
    "string": ["l_comment-string.csv", "l_linestatus-string.csv", "l_commitdate-string.csv", "l_receiptdate-string.csv", "l_returnflag-string.csv", "l_shipdate-string.csv", "l_shipinstruct-string.csv", "l_shipmode-string.csv"]
}

compression_techniques = ["bin","for","dif"]

def get_file_size(file_path):
    return os.path.getsize(file_path) if os.path.exists(file_path) else 0

def process_file(technique, data_type, original_file):
    # Skip unsupported combinations
    if data_type == "string" and technique in ["bin", "for","dif"]:
        print(f"Skipping {original_file} as {technique} does not support string data type.")
        return None

    encoded_file = f"{original_file}.{technique}"
    decoded_file = f"{encoded_file}.csv"

    encode_script = f"program-en-{technique}-{data_type}.py"
    decode_script = f"program-de-{technique}-{data_type}.py"
    encode_command = ["python", encode_script, original_file]
    decode_command = ["python", decode_script, encoded_file]

    start_time = time.time()
    subprocess.run(encode_command, check=True)
    encode_time = time.time() - start_time
    encoded_size = get_file_size(encoded_file)

    original_size = get_file_size(original_file)
    compression_ratio = original_size / encoded_size if encoded_size > 0 else 0

    start_time = time.time()
    subprocess.run(decode_command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    decode_time = time.time() - start_time
    decoded_size = get_file_size(decoded_file)

    return {
        "technique": technique,
        "data_type": data_type,
        "original_file": original_file,
        "encoded_file": encoded_file,
        "decoded_file": decoded_file,
        "original_size": original_size,
        "encoded_size": encoded_size,
        "decoded_size": decoded_size,
        "encode_time": encode_time,
        "decode_time": decode_time,
        "compression_ratio": compression_ratio,
    }

def main():
    print("Starting dynamic multi-core script...")
    results = []

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_file, technique, data_type, file)
                   for data_type, files in data_files.items()
                   for file in files
                   for technique in compression_techniques]

        for future in as_completed(futures):
            result = future.result()
            if result:
                results.append(result)

    with open("comparison_table.tex", "w") as tex_file:
        tex_file.write("\\begin{table}[h!]\n")
        tex_file.write("\\centering\n")
        tex_file.write("\\begin{tabular}{|c|c|c|c|c|c|c|c|}\n")
        tex_file.write("\\hline\n")
        tex_file.write("Technique & Data Type & Original File & Encoded File & Encoded Size (bytes) & Encoding Time (s) & Decoding Time (s) & Compression Ratio \\\\\n")
        tex_file.write("\\hline\n")

        for row in results:
            tex_file.write(f"{row['technique']} & {row['data_type']} & {row['original_file']} "
                           f"& {row['encoded_size']} & {row['encode_time']:.4f} & {row['decode_time']:.4f} & {row['compression_ratio']:.2f} \\\\\n")
            tex_file.write("\\hline\n")

        tex_file.write("\\end{tabular}\n")
        tex_file.write("\\caption{Comparison of encoding and decoding times, sizes, and compression ratios for different compression techniques and data types}\n")
        tex_file.write("\\end{table}\n")

    print("Comparison table generated in 'comparison_table.tex'.")

if __name__ == "__main__":
    main()
