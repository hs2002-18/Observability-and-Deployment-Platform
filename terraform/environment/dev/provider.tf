provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "Cloud-Observability-Platform"
      Environment = "Development"
      ManagedBy   = "Terraform"
    }
  }
}