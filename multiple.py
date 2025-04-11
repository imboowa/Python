import numpy as np

size_sqft = np.array([1500,1800,2100,2500,1700,2000])
bedrooms = np.array([3,4,3,5,3,4])
age = np.array([10,8,15,5,12,10])
price = np.array([300000,350000,330000,500000,280000,370000])

# Length of the data
data_len = len(price)

# Normalize variables
size_sqft_mean, size_sqft_std = np.mean(size_sqft), np.std(size_sqft)
bedrooms_mean, bedrooms_std = np.mean(bedrooms), np.std(bedrooms)
age_mean, age_std = np.mean(age), np.std(age)
price_mean, price_std = np.mean(price), np.std(price)

# Normalize each data input
scaled_size_sqft = (size_sqft - size_sqft_mean) / size_sqft_std
scaled_bedrooms = (bedrooms - bedrooms_mean) / bedrooms_std
scaled_age = (age - age_mean) / age_std
scaled_price = (price - price_mean) / price_std

# Initialize our parameters
w1, w2, w3, b, epoch, alpha = np.random.randn() * 0.01, np.random.randn() * 0.01, np.random.randn() * 0.01, np.random.randn() * 0.01, 10000, 1e-3

# Find the best parameters for this model
for _ in range(epoch):
    pred = (w1 * scaled_size_sqft) + (w2 * scaled_bedrooms) + (w3 * scaled_age) + b
    error = (scaled_price - pred)

    mse = (1 / data_len) * np.sum(error ** 2)

    d_mse_w1 = (-2 / data_len) * np.sum(error * scaled_size_sqft)
    d_mse_w2 = (-2 / data_len) * np.sum(error * scaled_bedrooms)
    d_mse_w3 = (-2 / data_len) * np.sum(error * scaled_age)
    d_mse_b = (-2 / data_len) * np.sum(error * 1)

    w1 = w1 - alpha * d_mse_w1
    w2 = w2 - alpha * d_mse_w2
    w3 = w3 - alpha * d_mse_w3
    b = b - alpha * d_mse_b

print(f"Final Weights and Biases\nW1: {w1}\nW2: {w2}\nW3: {w3}\nb: {b}\n")

def predict(size_sqft, bedrooms, age):
    scaled_size_sqft = (size_sqft - size_sqft_mean) / size_sqft_std
    scaled_bedrooms = (bedrooms - bedrooms_mean) / bedrooms_std
    scaled_age = (age - age_mean) / age_std
    scaled_prediction = (w1 * scaled_size_sqft) + (w2 * scaled_bedrooms) + (w3 * scaled_age) + b
    return (scaled_prediction * price_std) + price_mean

print(f"House Price :  ${predict(2200, 4, 8):,}")
print(f"House Price :  ${predict(1600, 3, 14):,}")
