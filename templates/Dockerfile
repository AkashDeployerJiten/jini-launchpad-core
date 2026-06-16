# Step 1: Standard Nginx image use karenge static site server karne ke liye
FROM nginx:alpine

# Step 2: HTML site ke saare contents ko Nginx ke default public HTML folder me copy karenge
COPY . /usr/share/nginx/html/

# Step 3: Port 80 expose karenge internet traffic ke liye
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]