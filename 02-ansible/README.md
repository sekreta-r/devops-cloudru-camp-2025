# Документация: Деплой echo-server с NGINX и Ansible

## Обоснование выбора алгоритма балансировки

Вместо стандартного round-robin алгоритма для балансировки нагрузки был выбран `least_conn`, так как он учитывает текущее количество активных соединений на каждом экземпляре сервиса. Это особенно актуально для echo-сервера, где запросы могут обрабатываться с разной скоростью, а нагрузка может быть неравномерной из-за поведения клиентов или случайных задержек. В отличие от round-robin, `least_conn` направляет запрос на наименее загруженный экземпляр, что делает его более адаптивным для масштабируемых Docker-сервисов.

```nginx
upstream echo_server {
    least_conn;
    server 127.0.0.1:8081;
    server 127.0.0.1:8082;
    server 127.0.0.1:8083;
}
```

### Старт плейбука

```bash
ansible-playbook playbooks/deploy_echo_server.yml --vault-password-file .vault_pass.txt
```

## Vault и защита креденшиалов

Для хранения кредов DockerHub (логин/токен) был использован **Ansible Vault**:

* Vault-файл: `group_vars/echo-node.yml`
* Vault-пароль: **123456789** (хранится в `.vault_pass.txt`)

### Команды работы с Vault:

```bash
# Шифрование
ansible-vault encrypt group_vars/echo-node.yml --vault-password-file .vault_pass.txt

# Чтение
ansible-vault view group_vars/echo-node.yml --vault-password-file .vault_pass.txt

# Редактирование
ansible-vault edit group_vars/echo-node.yml --vault-password-file .vault_pass.txt

# Дешифровка
ansible-vault decrypt group_vars/echo-node.yml --vault-password-file .vault_pass.txt
```

---

## Доступ к приватному регистри

* Создан токен для доступа только на чтение образов;
* Имя приватного репозитория: `sekretaria/echo-server:0.1.0`