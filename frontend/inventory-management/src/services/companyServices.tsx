import { getCompany } from '@/provider/Provider'

export async function getAllCompany() {
    const data = await getCompany();
    if (data) return data
    return new Error("Erro ao carregar a empresa")
}

