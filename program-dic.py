from argparse import ArgumentParser
import re
import time


def config_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("encoding", choices=("en", "de"))
    parser.add_argument("compression", choices=("bin", "rle", "dic", "for", "dif"))
    parser.add_argument("input_type", choices=("int8", "int16", "int32", "int64", "string"))
    parser.add_argument("file_path", type=str)
    return parser.parse_args()

def dic_encode(input_file,output_file):
    with open(input_file) as f:
        data=f.read().splitlines()

    dictionary = {}
    encode_data=[]
    i=0

    pattern = re.compile(r'(\b\w+\b|[^\w\s])')
    for line in data:
        if '-' in line and line.replace('-','').isdigit():
            parts = line.strip()
            if parts not in dictionary:
                    dictionary[parts] = i
                    i += 1
            encode_data.append([dictionary[parts]])
        else:
            parts=line.split()
            encode_linedata=[]
            for part in parts:
                texts = pattern.findall(part)
                for text in texts:
                    if text not in dictionary:
                        dictionary[text] = i
                        i += 1
                    encode_linedata.append(dictionary[text])
            encode_data.append(encode_linedata)

    with open(output_file,"w") as f:
        f.write("Dictionary:\n")
        for key,value in dictionary.items():
            line = f"{key}:{value}\n"
            if line.count(":") > 1:
               parts = line.split(":", 2)  
               line = f"{parts[0]}:{parts[1]}\n"  

            f.write(line)
        f.write("\nEncoded Data:\n")
        for line in encode_data:
            f.write(" ".join(map(str, line)) + "\n")

def dic_decode(input_file, output_file):
    dictionary = {}
    encoded_data = []

    with open(input_file) as f:
        reading_dict = True
        for line in f:
            line = line.strip()
            
            if line == "Encoded Data:":
                reading_dict = False
                continue
            
            if line == "Dictionary:":
                continue
    
            if reading_dict:
                if ":" in line:
                    key, value = line.split(":", 1)
                    if value.strip():  
                        dictionary[int(value.strip())] = key.strip()
            else:
                if line:  
                    encoded_data.append(list(map(int, line.split())))

    with open(output_file, "w") as f:
        for line in encoded_data:
            decoded_line = []
            for code in line:
                decoded_line.append(dictionary[code])
            decoded_string = " ".join(decoded_line).strip()
            cleaned_string = re.sub(r'\s+([,.!?;:-])', r'\1', decoded_string)
            cleaned_string = re.sub(r'([,.!?;:-])\s+([,.!?;:-])', r'\1\2', cleaned_string)
            cleaned_string = cleaned_string.replace("- ray", "-ray")
            cleaned_string = cleaned_string.replace("x- r", "x-r")
            f.write(cleaned_string + "\n") 

def main(args):
    encoding = args.encoding
    compression = args.compression
    input_type = args.input_type
    file_path = args.file_path

    # Determine which method to use
    if encoding == "en" and compression == "dic":
        dic_encode(file_path, file_path+'.dic')
    elif encoding == "de" and compression == "dic":
        dic_decode(file_path, file_path+'.csv')
    else:
        raise Exception("ERROR: Not yet implemented :p")

if __name__ == "__main__":
    main(config_parser())