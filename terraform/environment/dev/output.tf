output "vpc_id" {
  value = module.vpc.vpc_id
}

output "public_subnet_id" {
  value = module.vpc.public_subnet_id
}

output "security_group_id" {
  value = module.security_group.security_group_id
}

output "instance_profile_name" {
  value = module.iam.instance_profile_name
}

output "role_name" {
  value = module.iam.role_name
}

output "ec2_public_ip" {
  value = module.ec2.public_ip
}

output "ec2_private_ip" {
  value = module.ec2.private_ip
}

output "instance_id" {
  value = module.ec2.instance_id
}