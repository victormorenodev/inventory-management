import styles from '@/styles/table.module.css'
import { useEffect, useState } from 'react'
import {getAllProducts} from '@/services/productServices'
import {getAllSuppliers} from '@/services/supplierServices'

// Table component for inventory screen
export default function Table() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const result = await getAllProducts();
                if (result) {
                    setProducts(result);
                } else {
                    setProducts([]);
                }
            } catch (error) {
                console.error('Error in Table fetching products: ', error);
            }
        };
        fetchProducts();
    }, []);

    return (
        <div>
            <p>Lista de produtos: </p>
            <p>{products.map(product => product)
            }</p>
        </div>
    )
}