JWKS = {
    "keys": [
        {
            "e": "AQAB",
            "kid": "f86d695a3866466fbf57a5fea5f56cc9",
            "kty": "RSA",
            "n": "zUy8BsruXBWunO8JxXBcoyd2NXjsw-e5SnbIxijNHeTaHOGyckHh7QwXczDZonOfDdA1mhFjeH6JD7rMYymZqlNicx0zI5tEp0WPo2AiyPvY6XyxGAj3rPM0c94UtvaZs3m3kPKNWgIdkmtBVnR58OH75_RGvBoPTin6PJrIfrIOe_mctpwPmwmpqH23yVQZXffiL9LTLPgzLtS31j0Oh2Cia7AuZtjynGdtaV2x_ghnh8kJp6OgPVOF-NXVE2Ko-SHS3g_zpxDG94ig3Odvla00SX4rt-vZEHlvnNBXZQ4kXTFC2lQ7waf_U6LfolgOJAYKUuCrvF5T9VTr_ZCr-w",
            "use": "sig",
            "x5c": [
                "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"
            ],
            "x5t": "ZjJkOGQ0ODkyOWM3MTA3MDk2MTI0MTM5MmNiYWY0Yzg3MjY4ZDgxMA"
        }
    ]
}
X5C = JWKS['keys'][0]['x5c'][0]
X5T = JWKS['keys'][0]['x5t']
JWT = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IlpqSmtPR1EwT0RreU9XTTNNVEEzTURrMk1USTBNVE01TW1OaVlXWTBZemczTWpZNFpEZ3hNQSJ9.eyJpc3MiOiJodHRwczovL2FwaS5ieXUuZWR1IiwiZXhwIjoxNTQ1NDI1NzEwLCJodHRwOi8vd3NvMi5vcmcvY2xhaW1zL3N1YnNjcmliZXIiOiJCWVUvbmRwZXRlMjEiLCJodHRwOi8vd3NvMi5vcmcvY2xhaW1zL2FwcGxpY2F0aW9uaWQiOiIyMjQ2IiwiaHR0cDovL3dzbzIub3JnL2NsYWltcy9hcHBsaWNhdGlvbm5hbWUiOiJEZWZhdWx0QXBwbGljYXRpb24iLCJodHRwOi8vd3NvMi5vcmcvY2xhaW1zL2FwcGxpY2F0aW9udGllciI6IlVubGltaXRlZCIsImh0dHA6Ly93c28yLm9yZy9jbGFpbXMvYXBpY29udGV4dCI6Ii9lY2hvL3YxIiwiaHR0cDovL3dzbzIub3JnL2NsYWltcy92ZXJzaW9uIjoidjEiLCJodHRwOi8vd3NvMi5vcmcvY2xhaW1zL3RpZXIiOiJVbmxpbWl0ZWQiLCJodHRwOi8vd3NvMi5vcmcvY2xhaW1zL2tleXR5cGUiOiJQUk9EVUNUSU9OIiwiaHR0cDovL3dzbzIub3JnL2NsYWltcy91c2VydHlwZSI6IkFQUExJQ0FUSU9OIiwiaHR0cDovL3dzbzIub3JnL2NsYWltcy9lbmR1c2VyIjoibmRwZXRlMjFAY2FyYm9uLnN1cGVyIiwiaHR0cDovL3dzbzIub3JnL2NsYWltcy9lbmR1c2VyVGVuYW50SWQiOiItMTIzNCIsImh0dHA6Ly93c28yLm9yZy9jbGFpbXMvY2xpZW50X2lkIjoiSWp3UFFDNWVXU0daU0w2bFFCb1h1SG5IeXZzYSIsImh0dHA6Ly9ieXUuZWR1L2NsYWltcy9jbGllbnRfcmVzdF9vZl9uYW1lIjoiTmF0aGFuIEQiLCJodHRwOi8vYnl1LmVkdS9jbGFpbXMvY2xpZW50X3BlcnNvbl9pZCI6IjAwMzI3OTAzMiIsImh0dHA6Ly9ieXUuZWR1L2NsYWltcy9jbGllbnRfc29ydF9uYW1lIjoiUGV0ZXJzb24sIE5hdGhhbiBEIiwiaHR0cDovL2J5dS5lZHUvY2xhaW1zL2NsaWVudF9jbGFpbV9zb3VyY2UiOiJDTElFTlRfU1VCU0NSSUJFUiIsImh0dHA6Ly9ieXUuZWR1L2NsYWltcy9jbGllbnRfbmV0X2lkIjoibmRwZXRlMjEiLCJodHRwOi8vYnl1LmVkdS9jbGFpbXMvY2xpZW50X3N1YnNjcmliZXJfbmV0X2lkIjoibmRwZXRlMjEiLCJodHRwOi8vYnl1LmVkdS9jbGFpbXMvY2xpZW50X25hbWVfc3VmZml4IjoiICIsImh0dHA6Ly9ieXUuZWR1L2NsYWltcy9jbGllbnRfc3VybmFtZSI6IlBldGVyc29uIiwiaHR0cDovL2J5dS5lZHUvY2xhaW1zL2NsaWVudF9zdXJuYW1lX3Bvc2l0aW9uIjoiTCIsImh0dHA6Ly9ieXUuZWR1L2NsYWltcy9jbGllbnRfbmFtZV9wcmVmaXgiOiIgIiwiaHR0cDovL2J5dS5lZHUvY2xhaW1zL2NsaWVudF9ieXVfaWQiOiIwNzMxNzc2MTEiLCJodHRwOi8vYnl1LmVkdS9jbGFpbXMvY2xpZW50X3ByZWZlcnJlZF9maXJzdF9uYW1lIjoiTmF0aGFuIn0.lNNWfRiGo4KJPQHEOLqWpX8ZOAKE-e8xRx_xdyqPHVbi8O8-9cLxT6CX72_bFw2sZqTbncE0KEltVnC_Qspuov7GWN6_oH7Jc4ASehMKhMrJl1MqQ_NbGhoTedE0xr8cFqWjkBnx8_c-HpqvXwRaut7EYBuxPogok05Iu048yD0SlLQ75kjcdZ8IhcpPVKkQZiJr0KJvCRi8-LbYEZovF4KsJdzxQknkshY-XG7sVru7UxwTPvTS3YhW6_DUVy2WPDB5uCUkz4VFsGGvTDj1cHILxzHH3U7vFdB5llgb5eYUL2WBuGj1odzOUwaTOiSmmrsgNU5LijCMWZ1l1NK5yw"