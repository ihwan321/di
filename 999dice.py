import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzLGpzb24sdGltZSxzeXMscmFuZG9tLG9zLGFyZ3BhcnNlCmltcG9ydCBjb2xvcmFtYSxwbGF0Zm9ybQpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlLCBCYWNrLCBTdHlsZQpmcm9tIHJhbmRvbSBpbXBvcnQgcmFuZGludApmcm9tIGRhdGV0aW1lIGltcG9ydCBkYXRldGltZQpjb2xvcmFtYS5pbml0KGF1dG9yZXNldD1UcnVlKQoKCgpwYXJzZXIgPSBhcmdwYXJzZS5Bcmd1bWVudFBhcnNlcihkZXNjcmlwdGlvbj0nOTk5IERpY2UgQm90IHwgVGhpcyBJcyBHYW1ibGluZyBCb3QgUGxhc2UgVGFrZSBPd24gWW91ciBSaXNrJykKcGFyc2VyLmFkZF9hcmd1bWVudCgKICAgICctYycsJy0tYmV0c2V0JywKICAgIGRlZmF1bHQ9MCwKICAgIGhlbHA9J0VudGVyIFlvdXIgQmV0c2V0IE51bWJlciAoZGVmYXVsdDogMCknCikKbXlfbmFtZXNwYWNlID0gcGFyc2VyLnBhcnNlX2FyZ3MoKQoKCndpdGggb3BlbignY29uZmlnLmpzb24nLCAncicpIGFzIG15ZmlsZToKICAgICAgZGF0YT1teWZpbGUucmVhZCgpCiMgcGFyc2UgZmlsZQpvYmogPSBqc29uLmxvYWRzKGRhdGEpCgoKcHJpbnQgKFN0eWxlLk5PUk1BTCtGb3JlLk1BR0VOVEErIiAgICAgIF9fXyAgXyAgICAgICAgICAgX19fICAgICAgIF9fXG4gICAgIC8gXyBcKF8pX19fX19fICAgLyBfIClfX18gIC8gL19cbiAgICAvIC8vIC8gLyBfXy8gLV8pIC8gXyAgLyBfIFwvIF9fL1xuICAgL19fX18vXy9cX18vXF9fLyAvX19fXy9cX19fL1xfXy8iK1N0eWxlLk5PUk1BTCtGb3JlLkdSRUVOKyJcbj09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVxuIitTdHlsZS5CUklHSFQrRm9yZS5SRUQrIlxuICAgICAgICAgVGhpcyBJcyBHYW1ibGluZyBCb3RcbiAgICAgICBQbGVhc2UgVGFrZSBPd24gWW91ciBSaXNrXG4iKQoKaGlqYXUgPSBTdHlsZS5CUklHSFQrRm9yZS5HUkVFTgoKcmVzID0gU3R5bGUuUkVTRVRfQUxMCmFidTIgPSBTdHlsZS5OT1JNQUwrRm9yZS5XSElURQp1bmd1ID0gU3R5bGUuTk9STUFMK0ZvcmUuTUFHRU5UQQpoaWphdTIgPSBTdHlsZS5OT1JNQUwrRm9yZS5HUkVFTgpyZWQyID0gU3R5bGUuTk9STUFMK0ZvcmUuUkVECnJlZCA9IFN0eWxlLkJSSUdIVCtGb3JlLlJFRApjID0gcmVxdWVzdHMuc2Vzc2lvbigpCgp1cmwgPSAiaHR0cHM6Ly93d3cuOTk5ZG9nZS5jb20vYXBpL3dlYi5hc3B4Igp1YSA9IHsKICJPcmlnaW4iOiAiZmlsZTovLyIsCiAidXNlci1hZ2VudCI6IG9ialsiVXNlci1BZ2VudCJdLAogIkNvbnRlbnQtdHlwZSI6ICJhcHBsaWNhdGlvbi94LXd3dy1mb3JtLXVybGVuY29kZWQiLAogIkFjY2VwdCI6ICIqLyoiLAogIkFjY2VwdC1MYW5ndWFnZSI6ICJpZC1JRCxpZDtxPTAuOSxlbi1VUztxPTAuOCxlbjtxPTAuNyIsCiAiWC1SZXF1ZXN0ZWQtV2l0aCI6ICJjb20ucmVsYW5kLnJlbGFuZGljZWJvdCIKfQoKCmRlZiBrb252ZXJ0KHBlcnNlbix0YXJ1aGFuKToKICAgIGdsb2JhbCBoaWdoCiAgICBnbG9iYWwgbG93CiAgICBjID0gc3RyKDk5OTk5OSAqIGZsb2F0KHBlcnNlbikgLyAxMDApCiAgICBpZiB0YXJ1aGFuID09ICJIaSIgb3IgdGFydWhhbiA9PSAiaGkiIG9yIHRhcnVoYW4gPT0gIkhJIjoKICAgICAgIG4gPSBzdHIoYy5zcGxpdCgiLiIpWzFdKQogICAgICAgcGFuZ2thdCA9IDYgLSBsZW4obikKICAgICAgIGxvdyA9IGludChpbnQobikgKiAoMTAgKiogcGFuZ2thdCkpCiAgICAgICBoaWdoID0gOTk5OTk5CiAgICBpZiB0YXJ1aGFuID09ICJMbyIgb3IgdGFydWhhbiA9PSAiTE9XIiBvciB0YXJ1aGFuID09ICJsb3ciIG9yIHRhcnVoYW4gPT0gIkxvdyIgb3IgdGFydWhhbiA9PSAiTE8iOgogICAgICAgbG93ID0gMAogICAgICAgaGlnaCA9IGludChjLnNwbGl0KCIuIilbMF0pCgoKZGVmIHJldihudW0pOgogICAgaWYgKGxlbihudW0pIDwgOCk6CiAgICAgICAgcGFuamFuZ19ub2wgPSBpbnQoOCAtIGxlbihudW0pKQogICAgICAgIG51bSA9ICgocGFuamFuZ19ub2wqIjAiKStzdHIobnVtKSkKICAgICAgICByZXN1bHQgPSAoIjAuIitudW0pCiAgICBpZiAobGVuKG51bSkgPT0gOCk6CiAgICAgICAgcGFuamFuZ19ub2wgPSBpbnQoOCAtIGxlbihudW0pKQogICAgICAgIG51bSA9ICgocGFuamFuZ19ub2wqIjAiKStzdHIobnVtKSkKICAgICAgICByZXN1bHQgPSAoIjAuIitudW0pCiAgICBlbHNlOgogICAgICAgIGxlbl9udW0gPSBsZW4obnVtKQogICAgICAgIGVuZCA9IG51bVstODpdCiAgICAgICAgZmlyc3QgPSBudW1bOmxlbl9udW0tOF0KICAgICAgICByZXN1bHQgPSAoZmlyc3QrIi4iK2VuZCkKICAgIHJldHVybiAocmVzdWx0KQoKCmRlZiBkaWNlKHdzLGxzKToKICAgaWYgbXlfbmFtZXNwYWNlLmJldHNldCA9PSAiQXV0byIgb3IgbXlfbmFtZXNwYWNlLmJldHNldCA9PSAiYXV0byIgb3IgbXlfbmFtZXNwYWNlLmJldHNldCA9PSAiQVVUTyI6CiAgICAgIHVydXQgPSAwCiAgICAgIGp1bWxhaHVsYW5nPSAwCiAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgIGp1bWxhaHVsYW5nKz0xCiAgICAgICAgIHRyeToKICAgICAgICAgICAgIHBlc2FuID0gb2JqWyJDb25maWciXVtqdW1sYWh1bGFuZ11bIk5hbWUgQmV0IFNldCJdCiAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgIGJyZWFrCiAgIGVsc2U6CiAgICAgIHVydXQgPSBpbnQobXlfbmFtZXNwYWNlLmJldHNldCkKICAgICAgIAoKICAgc2xwID0gaW50KG9ialsiQ29uZ'
love = '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TxvPvNtVPNtVPNtVPNtVTyzVTWyqTyhM19lo2kyVQ09VPWVnFV6PvNtVPNtVPNtVPNtVPNtVPOlo2kyLzI0VQ0tVxucVtbtVPNtVPNtVPNtVPNtVPNtoz9spz9fMJWyqPN9VQNXVPNtVPNtVPOyoTyzVT9vnyfvD29hMzyaVy1oqKW1qS1oVxWyqPWqJlWVnFNiVRkiqlWqJlWHo2qaoTHvKFN9CFNvG24vVT9lVT9vnyfvD29hMzyaVy1oqKW1qS1oVxWyqPWqJlWVnFNiVRkiqlWqJlWHo2qaoTHvKFN9CFNvG04vVT9lVT9vnyfvD29hMzyaVy1oqKW1qS1oVxWyqPWqJlWVnFNiVRkiqlWqJlWHo2qaoTHvKFN9CFNvo24vBtbtVPNtVPNtVPNtVPOho19lo2kyLzI0VPf9ZDbtVPNtVPNtVPNtVPOcMvOmqTS0p19lo2kyLzI0K3qcovOcplOHpaIyBtbtVPNtVPNtVPNtVPNtVPOcMvOho19lo2kyLzI0VQ4tnJ50XT9vnyfvD29hMzyaVy1oqKW1qS1oVxWyqPWqJlWVnFNiVRkiqlWqJlWWMvOKnJ4vKFxtYFNkBtbtVPNtVPNtVPNtVPNtVPNtVPOlo2kyLzI0VQ0tVxkiVtbtVPNtVPNtVPNtVPNtVPOcMvOho19lo2kyLzI0VQ4tnJ50XT9vnyfvD29hMzyaVy1oqKW1qS1oVxWyqPWqJlWVnFNiVRkiqlWqJlWWMvOKnJ4vKFxtXvNlVP0tZGbXVPNtVPNtVPNtVPNtVPNtVPNtpz9fMJWyqPN9VPWVnFVXVPNtVPNtVPNtVPNtVPNtVPNtoz9spz9fMJWyqPN9VQNXVPNtVPNtVPNtVPNtnJLtp3EuqUAspz9fMJWyqS9fo3AyVTymVSElqJH6PvNtVPNtVPNtVPNtVPNtVTyzVT5iK3WioTIvMKDtCvOcoaDbo2WdJlWQo25znJpvKIg1paI0KIfvDzI0Vy1oVxucVP8tGT93Vy1oVxyzVRkip2HvKFxtYGRtBtbtVPNtVPNtVPNtVPNtVPNtVPOlo2kyLzI0VQ0tVxkiVtbtVPNtVPNtVPNtVPNtVPOcMvOho19lo2kyLzI0VQ4tnJ50XT9vnyfvD29hMzyaVy1oqKW1qS1oVxWyqPWqJlWVnFNiVRkiqlWqJlWWMvOZo3AyVy'
god = '0pICogMiAtIDE6CiAgICAgICAgICAgICAgICAgIHJvbGViZXQgPSAiSGkiCiAgICAgICAgICAgICAgICAgIG5vX3JvbGViZXQgPSAwCiAgICAgICAgZWxzZToKICAgICAgICAgICAgICByb2xlYmV0ID0gb2JqWyJDb25maWciXVt1cnV0XVsiQmV0Il1bIkJldCJdCiAgICAgICAgaWYgbXlfbmFtZXNwYWNlLmJldHNldCA9PSAiQXV0byIgb3IgbXlfbmFtZXNwYWNlLmJldHNldCA9PSAiQVVUTyIgb3IgbXlfbmFtZXNwYWNlLmJldHNldCA9PSAiYXV0byI6CiAgICAgICAgICB3YWt0dSA9IGRhdGV0aW1lLm5vdygpLnN0cmZ0aW1lKCclTScpCiAgICAgICAgICBpZiBpbnQod2FrdHUpID4gaW50KG1lbml0IC0gMSk6CiAgICAgICAgICAgICBtZW5pdCA9IGludChtZW5pdCkgKyBpbnQob2JqWyJJbnRlcnZhbCJdKQogICAgICAgICAgICAgdXJ1dCArPTEKICAgICAgICAgICAgIGlmIHVydXQgPT0ganVtbGFodWxhbmc6CiAgICAgICAgICAgICAgICB1cnV0ID0gMAogICAgICAgICAgICAgcHJpbnQgKCJDaGFuZ2UgQmV0IFNldCAiK29ialsiQ29uZmlnIl1bdXJ1dF1bIk5hbWUgQmV0IFNldCJdKyIgICAgICAgICAgICAgICAgICAgICAgICAgICAiKQogICAgICAgICAgICAgc2xwID0gaW50KG9ialsiQ29uZmlnIl1bdXJ1dF1bIkludGVydmFsIl0pIC8gMTAwMAogICAgICAgICAgICAgbGltaXRfYSA9IGludChvYmpbIkNvbmZpZyJdW3VydXRdWyJSZXNldCBJZiBXaW4iXSkgLSAxCiAgICAgICAgICAgICBwYXlpbiA9IGludChmbG9hdChvYmpbIkNvbmZpZyJdW3VydXRdWyJCYXNlIEJldCJdKSooMTAgKiogOCkpCgogICAgICAgIGVsc2U6CiAgICAgICAgICB1cnV0ID0gaW50KG15X25hbWVzcGFjZS5iZXRzZXQpCgogICAgICAgIGlmIG9ialsiQ29uZmlnIl1bdXJ1dF1bIlJhbmRvbSBDaGFuY2UiXVsiVG9nZ2xlIl0gPT0gIk9OIiBvciBvYmpbIkNvbmZpZyJdW3VydXRdWyJSYW5kb20gQ2hhbmNlIl1bIlRvZ2dsZSJdID09ICJPbiIgb3Igb2JqWyJDb25maWciXVt1cnV0XVsiUmFuZG9tIENoYW5jZSJdWyJUb2dnbGUiXSA9PSAib24iOgogICAgICAgICAgIGhhc2lsX2NoYW5jZSA9IHJvdW5kKHJhbmRvbS51bmlmb3JtKGZsb2F0KG9ialsiQ29uZmlnIl1bdXJ1dF1bIlJhbmRvbSBDaGFuY2UiXVsiTWluIl0pLGZsb2F0KG9ialsiQ29uZmlnIl1bdXJ1dF1bIlJhbmRvbSBDaGFuY2UiXVsiTWF4Il0pKSwyKQogICAgICAgICAgIGNvayA9IGxlbihzdHIoaGFzaWxfY2hhbmNlKSkKICAgICAgICAgICBpZiBjb2sgPT0gMzoKICAgICAgICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKCJcciIrc3RyKGhhc2lsX2NoYW5jZSkrIiAgICIpCiAgICAgICAgICAgaWYgY29rID09IDQ6CiAgICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgiXHIiK3N0cihoYXNpbF9jaGFuY2UpKyIgICIpCiAgICAgICAgICAgaWYgY29rID09IDU6CiAgICAgICAgICAgICAgc3lzLnN0ZG91dC53cml0ZSgiXHIiK3N0cihoYXNpbF9jaGFuY2UpKyIgIikKICAgICAgICAgICBrb252ZXJ0KGhhc2lsX2NoYW5jZSxzdHIocm9sZWJldCkpCiAgICAgICAgZWxzZToKICAgICAgICAgICBrb252ZXJ0KG9ialsiQ29uZmlnIl1bdXJ1dF1bIkNoYW5jZSJdLHN0cihyb2xlYmV0KSkKICAgICAgICB0aW1lLnNsZWVwKGZsb2F0KHNscCkpCiAgICAgICAgYW1vdW50ID0gaW50KGFtb3VudCkKICAgICAgICBuKz0xCiAgICAgICAgZGF0YSA9IHsKICAgICAgICAgICJhIjogIlBsYWNlQmV0IiwKICAgICAgICAgICJzIjoganNbIlNlc3Npb25Db29raWUiXSwKICAgICAgICAgICJQYXlJbiI6IGFtb3VudCwKICAgICAgICAgICJMb3ciOiBsb3csCiAgICAgICAgICAiSGlnaCI6IGhpZ2gsCiAgICAgICAgICAiQ2xpZW50U2VlZCI6IHJhbmRpbnQoMCw5OTk5OTkpLAogICAgICAgICAgIkN1cnJlbmN5IjogImRvZ2UiLAogICAgICAgICAgIlByb3RvY29sVmVyc2lvbiI6ICIyIgogICAgICAgIH0KICAgICAgICBpZiBwcm9mID4gZmxvYXQob2JqWyJUYXJnZXQgUHJvZml0Il0pOgogICAgICAgICAgIHByaW50IChoaWphdSsiXG5ZYXkuISBcblByb2ZpdCBNZW5jYXBhaSBUYXJnZXQuLi4uLiFcbiIraGlqYXUrIlByb2ZpdCAiK3JlcytzdHIocHJvZikpCiAgICAgICAgICAgc3lzLmV4aXQoKQogICAgICAgIHIxID0gYy5wb3N0KHVybCxoZWFkZXJzPXVhLGRhdGE9ZGF0YSkKICAgICAgICBqc24gPSBqc29uLmxvYWRzKHIxLnRleHQpCiAgICAgICAgcHJvZiA9IChmbG9hdChqc25bIlN0YXJ0aW5nQmFsYW5jZSJdICsgaW50KGpzblsiUGF5T3V0Il0pIC0gaW50KGFtb3VudCkgLSBqdW1ibCkvKDEwICoqIDgpKQogICAgICAgIGp1bSA9IGludChqc25bIlBheU91dCJdKSAtIGludChhbW91bnQpCiAgICAgICAgaWYganNuWyJTdGFydGluZ0JhbGFuY2UiXSA+IHdzOgogICAgICAgICAgIHByaW50ICh1bmd1KyJbIityZXMrc3RyKHJvbGViZXQpK3VuZ3UrIl0gIitoaWphdTIrc3RyKGZsb2F0KGFtb3VudCkvKDEwICoqIDgpKStoaWphdSsiIFsgIityZXMrc3RyKGZsb2F0KGludChqc25bIlN0YXJ0aW5nQmFsYW5jZSJdKSArIGludChqdW0pKS8oMTAgKiogOCkpK2hpamF1MisiIF0gIitoaWphdTIrIlByb2ZpdCIrcmVzK3N0cihwcm9mKSkKICAgICAgICAgICBwcmludCAoaGlqYXUrIlxuWW9zaC4uLiFcbkJhbGFuY2UgU3VkYWggTWVtZW51aGkgVGFyZ2V0Li4uLi4hIikKICAgICAgICAgICB0aW1lLnNsZWVwKDEpCiA'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))