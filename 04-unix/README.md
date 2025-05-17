# Запереть контейнер изнутри

Сработал метод — удаление DNS-серверов через обнуление `/etc/resolv.conf`.

## Этапы

1. Создан контейнер:

```bash
docker run -it --rm ubuntu bash
```

2. Проверен доступ к интернету:

```bash
apt-get update
```

3. Все попытки ограничения сети (через `iptables` и `ip route`) закончились сообщениями:

```
Operation not permitted
```

Причина: в контейнере отсутстует capability `CAP_NET_ADMIN`, необходимая для iptables и ip route.

---

## Решение: стереть DNS

```bash
echo "" > /etc/resolv.conf
```

Файл `/etc/resolv.conf` определяет DNS-серверы, через которые контейнер разрешает имена хостов (напр., archive.ubuntu.com).

Удаление всех записей делает контейнер невоспособным к разрешению DNS-имен, что влечёт ошибки при `apt-get update`, `ping`, `curl`
