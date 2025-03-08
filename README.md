# Proxmox Notifier
Discord notification can push to different channel based on different webhook.<br/><br/>
Your `.env` should be defined like the following (note no space between = key and value):
```env
manga_dc="WEBHOOK_URL"
zfs_dc="WEBHOOK_URL"
```
I use `channelName`\_dc as a convention to know exactly which channel this webhook link will push to.
## Application side
In application, I just need to define `POST` to `http://localhost:88/send` request with following parameters:<br/>
`channel` will be what you defined in `.env` without `_dc` portion.
```python
form = {
    "send_method": "discord",
    "channel": "zfs", # key: zfs_dc in .env
    "payload": payload # This is your message
}
```
