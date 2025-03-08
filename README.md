# Proxmox Notifier
Discord notification can push to different channel based on different webhook.<br/><br/>
Your json `dc_webhook-pass.json` should be defined as a valid `json` file like the following:
```json
{
  "manga_dc": "WEBHOOK_URL",
  "zfs_dc": "WEBHOOK_URL"
}
```
I use `channelName`\_dc as a convention to know exactly which channel this webhook link will push to.
## Docker secret
This json file should be stored as docker secret `dc_webhook-pass` via
```bash
docker secret dc_webhook-pass YOUR_JSON_FILE.json
```
## Application side
In application, I just need to define `POST` to `http://localhost:88/send` request with following parameters:<br/>
`channel` will be what you defined in `dc_webhook-pass.json` without `_dc` portion.
```python
    json = {
        "send_method": "discord",
        "channel": "zfs", # key: zfs_dc in dc_webhook-pass
        "payload": payload # This is your message
    }
```
