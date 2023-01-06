{{- define "gitlab.name" -}}
{{- .Values.nameOverride -}}
{{- end -}}

{{- define "gitlab.label" -}}
{{- .Values.nameOverriede -}}
{{- end -}}

{{- define "gitlab.namespace" -}}
  {{- if .Values.namespaceOverride -}}
    {{- .Values.namespaceOverride -}}
  {{- else -}}
    {{- .Release.Namespace -}}
  {{- end -}}
{{- end -}}
