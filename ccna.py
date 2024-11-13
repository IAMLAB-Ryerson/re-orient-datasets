import os
import subprocess


IMAGE='nistmni/minc-toolkit:1.9.18'

def convert_mnc_to_nii(minc_root_dir, target_dir):
    """
    Convert MINC (.mnc) files to NIfTI (.nii.gz) format using Docker.
    
    Args:
        minc_root_dir (str): Root directory containing .mnc files. Can contain subdirectories.
        target_dir (str): Directory where converted .nii.gz files will be saved.
        
    The function:
        - Recursively searches for .mnc files in minc_root_dir
        - Uses the nistmni/minc-toolkit Docker image for conversion
        - Preserves filenames (changing only the extension)
        - Creates the target directory if it doesn't exist
        - Prints status messages for successful conversions and errors
    """
    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # Loop through all files in minc_root
    for root, _, files in os.walk(minc_root_dir):
        for file in files:
            if file.endswith('.mnc'):
                # Construct input and output paths
                input_path = os.path.join(root, file)
                output_file = file.replace('.mnc', '.nii.gz')
                output_path = os.path.join(target_dir, output_file)
                
                # Construct and run the docker command
                cmd = [
                    'docker', 'run',
                    '-v', f'{os.path.abspath(minc_root_dir)}:/data/input',
                    '-v', f'{os.path.abspath(target_dir)}:/data/output',
                    IMAGE,
                    'mnc2nii',
                    '-nii',
                    '-quiet',
                    f'/data/input/{os.path.relpath(input_path, minc_root_dir)}',
                    f'/data/output/{output_file}'
                ]
                
                try:
                    subprocess.run(cmd, check=True)
                    print(f'Converted {file} to {output_file}')
                except subprocess.CalledProcessError as e:
                    print(f'Error converting {file}: {e}')

if __name__ == '__main__':
    # Set your input and output directories here
    minc_root_dir = r'D:\data\CCNA\CCNA\FLAIR\MINC'  # Directory containing .mnc files
    target_dir = r'D:\temp\CCNA\FLAIR\NIfTI'  # Directory where .nii.gz files will be saved
    
    convert_mnc_to_nii(minc_root_dir, target_dir)