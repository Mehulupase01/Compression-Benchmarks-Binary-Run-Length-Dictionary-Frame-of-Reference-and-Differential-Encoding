# Compression Techniques Comparison: Binary, Run-Length, Dictionary, Frame of Reference, and Differential Encoding

## Description  
This project compares five lossless data compression techniques—Binary, Run-Length, Dictionary, Frame of Reference, and Differential Encoding—applied to integer and string CSV data. The performance is evaluated in terms of compression ratio, file size, and encoding/decoding time.

## Task / Problem Statement  
The task is to implement and compare the performance of five data compression techniques on various integer and string datasets. The goal is to evaluate the compression efficiency and speed of each technique and analyze their suitability for different types of data, such as integers and strings.

## Sub-Tasks  
1. **Implement Compression Techniques**: Implement five compression techniques: Binary, Run-Length, Dictionary, Frame of Reference, and Differential Encoding.  
2. **Test on Various Data Types**: Apply each technique to integer types (int8, int16, int32, int64) and strings.  
3. **Evaluate Compression Performance**: Measure and compare compression ratios, encoded file sizes, and encoding/decoding times for each technique.  
4. **Analyze Results**: Discuss the results and identify the most efficient techniques for different data types.

## Implementation Details  
### 1. **Binary Encoding (bin)**  
   - **Method**: Converts integers into machine-readable binary format, which reduces storage size compared to text-based formats.  
   - **Performance**: Offers fast encoding and decoding with moderate compression ratios. Best for scenarios requiring quick storage without heavy compression.

### 2. **Run-Length Encoding (rle)**  
   - **Method**: Replaces consecutive repeated values with a single value and its count. Ideal for data with long sequences of identical values.  
   - **Performance**: Effective on data with many consecutive repetitions, but not suitable for highly variable data.

### 3. **Dictionary Encoding (dic)**  
   - **Method**: Replaces repeated values with tokens from a dictionary. Effective for string data with many repetitive words or phrases.  
   - **Performance**: Performs well with string data but less effective for integer data with high variability.

### 4. **Frame of Reference Encoding (for)**  
   - **Method**: Encodes integer data by storing the differences from a reference value. Suitable for ordered data with small variations.  
   - **Performance**: Efficient for data with small deltas but less effective when the data is highly varied.

### 5. **Differential Encoding (dif)**  
   - **Method**: Encodes data by storing the difference between consecutive values. Ideal for sequential data with incremental changes.  
   - **Performance**: Achieves high compression ratios for sequential data but struggles with irregular or non-monotonic data.

## Program Breakdown  
The implementation consists of **26 programs** in total, divided as follows:

### 1. **Binary, Frame of Reference, and Differential Encoding**  
   - **8 Programs for Each Encoding Type**: 4 for encoding (int8, int16, int32, int64) and 4 for decoding (int8, int16, int32, int64).  
   - **To Run the Programs**:  
     
     #### Encode  
     ```bash
     python <program-en-for|bin|dif-int8|16|32|64.py> <Filename.csv> 
     ```

     #### Decode  
     ```bash
     python <program-de-for|bin|dif-int8|16|32|64.py> <Filename.csv.for|dif|bin> 
     ```

### 2. **Run-Length Encoding (rle.py) and Dictionary Encoding (program-dic.py)**  
   - **2 Programs for Encoding/Decoding**:  
     #### Run-Length Encoding  
     - **Encode**  
       ```bash
       python rle.py en|de rle int8|16|32|64 <file_path>
       ```
     - **Decode**  
       ```bash
       python rle.py en|de rle int8|16|32|64 <file_path>
       ```

     #### Dictionary Encoding  
     - **Encode**  
       ```bash
       python program-dic.py en|de dic int8|16|32|64 <file_path>
       ```
     - **Decode**  
       ```bash
       python program-dic.py en|de dic int8|16|32|64 <file_path>
       ```

## Metrics and Results

### **Compression Ratios**

| Technique         | File Type        | Compression Ratio |
|-------------------|------------------|-------------------|
| Binary Encoding   | int8, int16, int32, int64 | 0.25 to 2.00      |
| Run-Length Encoding | string, int8, int16 | 0.19 to 1.77      |
| Dictionary Encoding | string          | 0.70 to 2.42      |
| Frame of Reference | int8, int16, int32, int64 | 0.25 to 2.82      |
| Differential Encoding | int8, int16, int32, int64 | 0.26 to 2.82      |

### **Encoding and Decoding Times**

| Technique         | File Type        | Encoding Time (s) | Decoding Time (s) |
|-------------------|------------------|-------------------|-------------------|
| Binary Encoding   | int8, int16, int32, int64 | 1.5 to 2.5       | 1.5 to 2.5       |
| Run-Length Encoding | string          | 0.1 to 1.0        | 0.1 to 1.0        |
| Dictionary Encoding | string          | 2.0 to 5.0        | 5.0 to 8.0        |
| Frame of Reference | int8, int16, int32, int64 | 2.5 to 3.7       | 2.5 to 3.7       |
| Differential Encoding | int8, int16, int32, int64 | 2.0 to 3.0       | 1.5 to 3.0       |

## Conclusion  
- **Binary Encoding** provides a fast, efficient method for compacting integer data but offers limited compression.  
- **Run-Length Encoding** is highly effective for datasets with repeated values but performs poorly on more variable data.  
- **Dictionary Encoding** is best for string data with many repeated values, though it incurs computational and storage overhead for high-variance datasets.  
- **Frame of Reference Encoding** works well for integer data with small variations but suffers from file bloat with highly variable datasets.  
- **Differential Encoding** excels with sequential data and provides high compression ratios for data with small deltas.

## Future Work  
- **Hybrid Compression**: Investigate hybrid approaches that combine multiple techniques based on data characteristics.  
- **Performance Optimization**: Explore optimizations to improve encoding and decoding speeds, especially for large datasets.

## References  
- **Data Compression Techniques**: [Data Compression Algorithms](https://en.wikipedia.org/wiki/Data_compression)  
- **Python Implementation**: [Python Official Documentation](https://python.org)  
- **TPCH Dataset**: [TPCH Benchmark](http://www.tpc.org/tpch/)

