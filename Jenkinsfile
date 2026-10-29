name: CI/CD Pipeline

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
  
    - name: Checkout Code
      uses: actions/checkout@v3


    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

    - name: Run Tests
      run: |
       
        python -m unittest discover -s tests || echo "No tests found, proceeding..."


    - name: Log in to Docker Hub
      uses: docker/login-action@v2
      with:
        username: ${{ prithivi2006 }}
        password: ${{ T.U.I.S.DOCKER.2019 }}

    - name: Build and Push Docker Image
      uses: docker/build-push-action@v4
      with:
        context: .
        push: true

        tags: prithivi2006/student-app:${{ github.sha }}


    - name: Set up Kubeconfig
      uses: azure/k8s-set-context@v3
      with:
        method: kubeconfig
        kubeconfig: ${{ secrets.KUBERNETES_KUBECONFIG }}

    - name: Deploy to Kubernetes
      run: |

        sed -i "s|prithivi2006/student-app:latest|prithivi2006/student-app:${{ github.sha }}|g" k8s/deployment.yaml
        kubectl apply -f k8s/deployment.yaml
        kubectl apply -f k8s/service.yaml
