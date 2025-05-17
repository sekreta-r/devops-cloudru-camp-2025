# Kubernetes

В данном репозитории реализован деплой echo-server приложения в Kubernetes двумя способами (с использованием Ingress Controller):

* через **raw манифесты** (`/03-kubernetes/raw`)
* через **Helm chart** (`/03-kubernetes/helm/echo-server`)

---

## Развёртка Ingress Controller

1. Создание namespace:

```bash
kubectl create namespace ingress-nginx
```

2. Генерация манифеста ingress-nginx через Helm:

```bash
CHART_VERSION="4.12.1"
APP_VERSION="1.12.1"

helm template ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --version ${CHART_VERSION} \
  --namespace ingress-nginx \
  --create-namespace \
  --set controller.kind=DaemonSet \
  --set controller.daemonset.useHostPort=true \
  --set controller.hostPort.enabled=true \
  --set controller.hostPort.ports.http=80 \
  --set controller.service.type=ClusterIP \
  --set controller.ingressClassResource.default=true \
  --set controller.tolerations[0].key="node-role.kubernetes.io/control-plane" \
  --set controller.tolerations[0].operator="Exists" \
  --set controller.tolerations[0].effect="NoSchedule" \
  > ./03-kubernetes/nginx-ingress.${APP_VERSION}.yaml
```

3. Применение:

```bash
kubectl apply -f ./03-kubernetes/nginx-ingress.1.12.1.yaml
```

---

## Деплой способом raw (папка `/03-kubernetes/raw`)

Деплой:

```bash
kubectl apply -f ./03-kubernetes/raw -n var15
```

---

## Деплой способом Helm (папка `/03-kubernetes/helm/echo-server`)

Установка:

```bash
helm install echo-server ./03-kubernetes/helm/echo-server --namespace echo-server-namespace --create-namespace
```

Удаление:

```bash
helm uninstall echo-server --namespace echo-server-namespace
```

---