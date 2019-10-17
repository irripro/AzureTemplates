resource "docker_image" "ghost_image" {
  name = "${var.image_name}"
}

resource "docker_container" "ghost_container" {
  name  = "${var.container_name}"
  image = "${docker_image.ghost_image.latest}"

  ports {
    internal = "${var.int_port}"
    external = "${var.ext_port}"
  }
}
