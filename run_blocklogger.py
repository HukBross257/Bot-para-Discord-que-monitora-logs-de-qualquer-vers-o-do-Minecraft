from mcbridge import abrir_os_logs, mostrar_logs

with abrir_os_logs() as dados:
	mostrar_logs(dados)