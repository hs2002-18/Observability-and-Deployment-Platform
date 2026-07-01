provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project   = "Cloud-Observability-Platform"
      ManagedBy = "Terraform"
    }
  }
}