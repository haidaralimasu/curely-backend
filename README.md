# Curely backend

curely.in backend

## Requirements

- node v3.11.9

## Local Development

Clone the project and install dependencies.

```sh
git clone git@git.energi.software:energi/tech/dweb/nft/marketplace/launchpad/webapp.git launchpad-webapp
cd launchpad-webapp
yarn install
```

Depending on environment, copy environment file into `.env`:

- `.env.testnet` (testnet variables)
- `.env.mainnet` (mainnet variables)
- `.env.template` (variables have to be assigned manually)

**QA**

```sh
cp .env.template .env
yarn dev
```

**Testnet**

```sh
cp .env.testnet .env
yarn dev
```

### Deployment

```sh
cp .env.mainnet .env
yarn build
yarn start
```

### Lint

```
yarn lint
```

## Environmental Variables

| Variable                      | Description                                   |
| :---------------------------- | :-------------------------------------------- |
| REACT_APP_SERVER_URL          | General API URL                               |
| REACT_APP_USER_API_URL        | User API URL                                  |
| REACT_APP_ASSETS_INFO_API_URL | URL for fetching asset prices and information |
| REACT_APP_REFERRAL_API_URL    | Referral API URL                              |
| REACT_APP_NETWORK_NAME        | Network name (e.g. Energi)                    |
| REACT_APP_BUILD_MODE          | Network mode (Testnet/Mainnet)                |
