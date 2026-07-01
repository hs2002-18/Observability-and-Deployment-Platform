module "vpc" {
  source             = "../../modules/vpc"
  project_name       = var.project_name
  vpc_cidr           = var.vpc_cidr
  public_subnet_cidr = var.public_subnet_cidr
  availability_zone  = var.availability_zone
}

module "security_group" {
  source       = "../../modules/security"
  project_name = var.project_name
  vpc_id       = module.vpc.vpc_id
}

module "iam" {
  source       = "../../modules/iam"
  project_name = var.project_name
}

module "ec2" {

  source                = "../../modules/ec2"
  project_name          = var.project_name
  ami_id                = var.ami_id
  instance_type         = var.instance_type
  subnet_id             = module.vpc.public_subnet_id
  security_group_id     = module.security_group.security_group_id
  instance_profile_name = module.iam.instance_profile_name
  key_name              = var.key_name
  public_key_path       = var.public_key_path

}