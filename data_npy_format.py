import pandas as pd
import numpy as np
import os


def excel_to_npy_basic(excel_path, npy_path=None, sheet_name=0):
    """
    将Excel文件转换为NumPy的npy格式

    参数:
    excel_path: Excel文件路径
    npy_path: 输出的npy文件路径（默认为同目录同名文件）
    sheet_name: Excel工作表名称或索引

    返回:
    data: 转换后的NumPy数组
    """
    try:
        # 1. 读取Excel文件
        print(f"正在读取Excel文件: {excel_path}")
        df = pd.read_excel(excel_path, sheet_name=sheet_name)

        # 2. 显示数据信息
        print(f"数据形状: {df.shape}")
        print(f"列名: {list(df.columns)}")
        print(f"前几行数据:\n{df.head()}")

        # 3. 转换为NumPy数组
        data = df.to_numpy()
        print(f"NumPy数组形状: {data.shape}")
        print(f"数据类型: {data.dtype}")

        # 4. 确定输出路径
        if npy_path is None:
            base_name = os.path.splitext(excel_path)[0]
            npy_path = f"{base_name}.npy"

        # 5. 保存为npy文件
        np.save(npy_path, data)
        print(f"数据已保存到: {npy_path}")
        print(f"文件大小: {os.path.getsize(npy_path) / 1024:.2f} KB")

        # 6. 验证保存的数据
        loaded_data = np.load(npy_path, allow_pickle=True)
        print(f"验证加载 - 形状一致: {np.array_equal(data, loaded_data)}")

        return data

    except FileNotFoundError:
        print(f"错误: 找不到文件 {excel_path}")
        return None
    except Exception as e:
        print(f"错误: {str(e)}")
        return None


# 使用示例
if __name__ == "__main__":
    # 示例1: 基本使用
    excel_file = "./share_data/data.xlsx"  # 替换为您的Excel文件路径
    # data_array = excel_to_npy_basic(excel_file)

    data_array = excel_to_npy_basic(excel_file, "output_data.npy")

    # 示例3: 指定工作表
    # data_array = excel_to_npy_basic(excel_file, sheet_name="Sheet1")