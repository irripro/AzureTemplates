variable "image_name" {
  description = "Image for container"
  default     = "ghost:latest"
}

variable "container_name" {
  default     = "blog"
  description = "Name of the containe"
}

variable "ext_port" {
  description = "External port for container"
  default     = "80"
}
