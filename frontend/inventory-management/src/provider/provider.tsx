import axios from 'axios'

// Here in provider we have the functions that fetch data from the server

// Fetch the company
export async function getCompany() {
    try {
        const response = await axios.get(`${process.env.BASE_URL}/api/company`)
        return response.data;
    } catch (error) {
        console.log(error);
    }
}

// Fetch all the products
export async function getProduts() {
    try {
        const response = await axios.get(`${process.env.BASE_URL}/api/products`)
        return response.data;
    } catch (error) {
        console.log(error);
    }
}

// Fetch all the suppliers
export async function getSuppliers() {
    try {
        const response = await axios.get(`${process.env.BASE_URL}/api/suppliers`)
        return response.data;
    } catch (error) {
        console.log(error);
    }
}

// Fetch all the categories
export async function getCategories() {
    try {
        const response = await axios.get(`${process.env.BASE_URL}/api/categories`)
        return response.data;
    } catch (error) {
        console.log(error);
    }
}

// Fetch all the stockists
export async function getStockists() {
    try {
        const response = await axios.get(`${process.env.BASE_URL}/api/stockists`)
        return response.data;
    } catch (error) {
        console.log(error);
    }
}