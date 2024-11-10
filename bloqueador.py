import os
import platform
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from elevate import elevate
elevate(graphical=False)

# Função para obter o caminho do arquivo hosts dependendo do sistema operacional
def get_hosts_file():
    system = platform.system().lower()
    if system == 'windows':
        return r'C:\Windows\System32\drivers\etc\hosts'
    elif system == 'linux':
        return '/etc/hosts'
    else:
        raise Exception("Sistema operacional não suportado.")

# Função para bloquear sites
def bloquear_site(sites):
    hosts_file = get_hosts_file()

    try:
        # Solicitar permissão de root (admin) antes de modificar o arquivo hosts

        # Agora, modificamos o arquivo hosts
        with open(hosts_file, 'a') as f:
            for site in sites:
                # Adiciona o redirecionamento para 127.0.0.1 para bloquear o site
                f.write(f"127.0.0.1    {site}\n")
        
        messagebox.showinfo("Sucesso", "Sites bloqueados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao bloquear sites: {e}")

# Função para desbloquear sites
def desbloquear_site(sites):
    hosts_file = get_hosts_file()

    try:
        # Solicitar permissão de root (admin) antes de modificar o arquivo hosts

        # Lê o arquivo hosts e remove os sites bloqueados
        with open(hosts_file, 'r') as f:
            lines = f.readlines()

        with open(hosts_file, 'w') as f:
            for line in lines:
                if not any(site in line for site in sites):
                    f.write(line)
                else:
                    print(f"Removendo bloqueio do site: {line.strip()}")
        
        messagebox.showinfo("Sucesso", "Sites desbloqueados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao desbloquear sites: {e}")

# Função para obter os sites do usuário e chamar as funções de bloqueio/desbloqueio
def on_submit(block=True):
    sites_input = entry_sites.get("1.0", tk.END).strip()
    sites = [site.strip() for site in sites_input.splitlines() if site.strip()]

    if block:
        if sites:
            bloquear_site(sites)
        else:
            messagebox.showwarning("Aviso", "Por favor, insira pelo menos um site para bloquear.")
    else:
        if sites:
            desbloquear_site(sites)
        else:
            messagebox.showwarning("Aviso", "Por favor, insira pelo menos um site para desbloquear.")

# Configuração da interface gráfica com Tkinter
root = tk.Tk()
root.title("Bloqueador de Sites")
root.geometry("500x350")
root.config(bg="#f0f0f0")  # Cor de fundo

# Título
title_label = tk.Label(root, text="Bloqueador de Sites", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

# Descrição
desc_label = tk.Label(root, text="Digite os sites (um por linha) que deseja bloquear ou desbloquear:", font=("Helvetica", 12), bg="#f0f0f0", fg="#555")
desc_label.pack(pady=5)

# Campo de texto para os sites
entry_sites = scrolledtext.ScrolledText(root, height=8, width=40, font=("Helvetica", 12), bd=2, relief="groove", wrap=tk.WORD)
entry_sites.pack(pady=10)

# Botões
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

btn_block = tk.Button(btn_frame, text="Bloquear Sites", command=lambda: on_submit(block=True), bg="#ff6347", fg="white", font=("Helvetica", 12, "bold"), width=15, relief="flat")
btn_block.grid(row=0, column=0, padx=10)

btn_unblock = tk.Button(btn_frame, text="Desbloquear Sites", command=lambda: on_submit(block=False), bg="#4caf50", fg="white", font=("Helvetica", 12, "bold"), width=15, relief="flat")
btn_unblock.grid(row=0, column=1, padx=10)

# Rodapé
footer_label = tk.Label(root, text="© 2024 - Criado por Guilherme Morais", font=("Helvetica", 10), bg="#f0f0f0", fg="#777")
footer_label.pack(side="bottom", pady=10)

# Rodar o Tkinter
root.mainloop()
