resource "aws_eks_node_group" "node_group" {
  cluster_name    = aws_eks_cluster.eks_cluster.name
  node_group_name = "aws-devops-node-group"
  node_role_arn   = aws_iam_role.node_role.arn

  subnet_ids = [
    aws_subnet.public_subnet_1.id,
    aws_subnet.public_subnet_2.id
  ]

  scaling_config {
    desired_size = 1
    min_size     = 1
    max_size     = 1
  }

  instance_types = ["t3.micro"]

  capacity_type = "ON_DEMAND"

  depends_on = [
    aws_iam_role_policy_attachment.worker_node_policy,
    aws_iam_role_policy_attachment.cni_policy,
    aws_iam_role_policy_attachment.ecr_policy,
    aws_eks_cluster.eks_cluster
  ]

  tags = {
    Name = "aws-devops-node-group"
  }
}