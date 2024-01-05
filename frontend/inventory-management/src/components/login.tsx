import styles from '../styles/login.module.css' 

// Login screen component for login page
export default function Login() {
    return (
        <div className={styles.pageWrapper}>
            <div className={styles.loginScreen}>
                <p className="text-3xl">Tela de Login</p>
                <form>
                    <div>
                        <p>Email:</p>
                        <input type="email"/>
                    </div>
                    <div>
                        <p>Senha: </p>
                        <input type="password"/>
                    </div>
                    <button className={styles.button}>Entrar</button>
                </form>
            </div>  
        </div>
    )

}