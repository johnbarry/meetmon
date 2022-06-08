# meetmon

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
cd /c/work/vue
mkdir node
cd node
curl https://nodejs.org/dist/v16.15.0/node-v16.15.0-win-x64.zip > node.zip
unzip *zip
export PATH="$PATH:/c/work/vue/node/node-v16.15.0-win-x64"
cd /c/work/vue
gh repo clone johnbarry/meetmon
cd meetmon
npm install -g vue@latest
npm install @vitejs/plugin-vue
```

### Compile and Hot-Reload for Development

```sh
npm run dev

(now open http://localhost:3000)
```

### Compile and Minify for Production

```sh
npm run build
```
