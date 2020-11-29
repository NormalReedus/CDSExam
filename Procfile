heroku config:set HOST=0.0.0.0
heroku config:set NODE_ENV=production

web: sh -c 'cd nuxt'
web: npm run build
web: npm run start