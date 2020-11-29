heroku config:set HOST=0.0.0.0
heroku config:set NODE_ENV=production

web: sh -c 'cd nuxt'
web: nuxt build
web: nuxt start