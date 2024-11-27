from huggingface_hub import HfApi

# Set your access token, you can get it in HuggingFace website's personal setting
api = HfApi(token="XXX")

# upload you local folder path to the target HF repo address
api.upload_folder(
    folder_path="/root/VulLLM/data/VulResource",
    repo_id="xuefen/VulResource",
    repo_type="dataset",
)

print("Upload complete!")
