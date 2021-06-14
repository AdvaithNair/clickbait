# Base Image
FROM node:14 as base

# Current Directory Definition
WORKDIR /home/node/app

# Move Contents To Directory
COPY . ./

# Prepare for Build
EXPOSE 3000
ENV HOST=0.0.0.0
ENV PORT=3000

# Install Dependencies
RUN yarn

FROM base as production

# Build and Run Web
RUN yarn build
CMD [ "yarn", "start" ]