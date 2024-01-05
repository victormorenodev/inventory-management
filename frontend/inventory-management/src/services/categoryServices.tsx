import { getCategories } from '@/provider/Provider'

export async function getAllCategories() {
    const data = await getCategories();
    if (data) return data
    return new Error("Erro ao carregar as categorias")
}

