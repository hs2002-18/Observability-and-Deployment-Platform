variable "aws_region" {
  default = "ap-south-1"
  type    = string
}

variable "terraform_state_bucket" {
  default = "cop-s3-project-bucket"
  type    = string
}

variable "terraform_lock_table" {
  default = "terraform-lock-table"
  type    = string
}