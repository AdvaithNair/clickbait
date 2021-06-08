# Base Image
FROM node:14

# Current Directory Definition
WORKDIR /usr/src/app

# Move Contents To Directory
COPY . ./

# Install Dependencies
RUN yarn

# Prepare for Build
EXPOSE 8080
ENV HOST=0.0.0.0
ENV PORT=8080

# Build and Run Web
RUN yarn build
CMD [ "yarn", "start" ]