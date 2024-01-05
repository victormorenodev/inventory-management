import { getSuppliers } from '@/provider/Provider'

export async function getAllSuppliers() {
    const data = await getSuppliers();
    if (data) return data
    return new Error("Erro ao carregar os fornecedores")
}

