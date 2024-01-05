import { getStockists } from '@/provider/Provider'

export async function getAllStockists() {
    const data = await getStockists();
    if (data) return data
    return new Error("Erro ao carregar os usuários")
}

