FROM odoo:18.0

USER root

# Instala la biblioteca requests usando apt
RUN apt-get update && apt-get install -y python3-requests

USER odoo
