<template>
    <div class="bg-gray-100 min-h-screen">
        <div class="bg-gradient-to-r from-fuchsia-400 to-pink-400 mt-2 rounded shadow-sm border border-gray-300 py-8">

            <span class="flex items-center justify-center text-pink-100 font-bold text-xl"> Sign in</span>
            <span class="flex items-center justify-center text-pink-100 text-sm">Sign in to your account</span>

        </div>
        <div class=" w-full md:w-3/12 px-2 mx-auto mt-12">
            <form @submit.prevent="handleSubmit">
                <InputField id="username" label="Username" type="text" placeholder="Enter Username"
                    v-model="form.username" required />
                <InputField id="password" label="Password" type="password" placeholder="Enter Password"
                    v-model="form.password" required/>
                
                <div class="" v-if="form.errors.length">
                    <ul v-for="error in form.errors" v-bind:key="error">
                        <li class="bg-red-100 text-red-800 text-xs mb-2 ring-1 ring-red-200 text-center rounded p-2">{{
                            error }}
                        </li>
                    </ul>

                </div>
                <button type="submit"
                    :class="{ 'bg-violet-500 animate-pulse duration-300': isSubmitting, 'bg-violet-800 hover:bg-violet-900 duration-300': !isSubmitting }"
                    :disabled="isSubmitting" class="mb-4 text-white flex justify-center w-full rounded p-3 mt-6">Sign
                    in</button>
            </form>
            <div class="text-gray-600">
                <span>Don't have an account? </span>
                <router-link class="text-violet-800 font-bold hover:underline" to="/sign-up">Sign up</router-link> to
                create
                one
            </div>

        </div>
    </div>

</template>

<script>
import InputField from '@/components/InputField.vue'
import axios from 'axios'

export default {
    name: 'SignIn',
    components: {
        InputField
    },
    data() {
        return {
            form: {
                username: '',
                password: '',
                errors: []
            },
            isSubmitting: false
        };
    },
    methods: {
        async handleSubmit() {
            this.form.errors = []
            if (this.form.username === '') {
                this.form.errors.push('Username is Required')
            }
            if (this.form.password === '') {
                this.form.errors.push('Password is Required')
            }
            if (!this.form.errors.length) {
                this.isSubmitting = true;
                const formData = {
                    username: this.form.username,
                    password: this.form.password
                };
                try {
                    const response = await axios.post("/api/v1/token/login", formData);
                    const token = response.data.auth_token;
                    this.$store.commit('setToken', token);
                    localStorage.setItem("token", token);
                    await this.$store.dispatch('fetchUser');
                    const toPath = this.$route.query.to || '/dashboard';
                    this.$router.push(toPath);
                } catch (error) {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.form.errors.push(`${error.response.data[property]}`);
                        }
                    } else {
                        this.form.errors.push('Something went wrong. Please try again later.');
                        console.log(JSON.stringify(error));
                    }
                } finally {
                    this.isSubmitting = false;
                }
            }


        }
    },
    mounted() {
        document.title = 'Sign in | Lets Learn'
    }
}
</script>