import docker

def check_and_update_image(image_name):
    client = docker.from_env()

    try:
        image = client.images.get(image_name)  # 获取镜像详细信息
        client.images.pull(image_name)  # 拉取最新版本镜像
        print(f"镜像 {image_name} 已更新为最新版本。")
    except docker.errors.ImageNotFound:
        print(f"镜像 {image_name} 不存在，请确保镜像名称和标签正确。")

image_name = "beatrueman/monitoring:6.0"
check_and_update_image(image_name)

