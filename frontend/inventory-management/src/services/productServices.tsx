import { getProduts } from '@/provider/Provider'

export async function getAllProducts() {
    const data = await getProduts();
    
}
