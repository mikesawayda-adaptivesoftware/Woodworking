FROM nginxinc/nginx-unprivileged:stable-alpine

LABEL org.opencontainers.image.title="Entertainment Center Build Companion" \
      org.opencontainers.image.description="Woodworking plans, reference images and an interactive build checklist"

COPY --chown=101:101 deploy/nginx.conf /etc/nginx/conf.d/default.conf
COPY --chown=101:101 app/ /usr/share/nginx/html/app/
COPY --chown=101:101 docs/ /usr/share/nginx/html/docs/
COPY --chown=101:101 assets/ /usr/share/nginx/html/assets/

EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -q -O /dev/null http://127.0.0.1:8080/healthz || exit 1
