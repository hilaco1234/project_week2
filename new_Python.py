for root, directories, files in os.walk('.'):
    for _file in files:
        full_path = os.path.join(root, _file)
        print(f"File found: {full_path}")
