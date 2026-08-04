resource "aws_s3_bucket" "demo_bucket" {
  bucket = var.bucket_name

  tags = {
    Name        = "Terraform Demo Bucket"
    Environment = "Dev"
  }
}