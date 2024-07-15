<template>
    <div class="bg-gray-100 min-h-screen">
        <div class="bg-violet-100 mt-2 rounded py-8 text-gray-600">

            <span class="flex items-center justify-center font-bold text-xl"> Sign up</span>
            <span class="flex items-center justify-center text-sm">Sign up for an account</span>

        </div>
        <div class=" w-full md:w-3/12 px-2 mx-auto mt-12">
            <form @submit.prevent="handleSubmit">
                <InputField id="first_name" label="First Name" type="text" placeholder="Enter First Name"
                    v-model="form.first_name" required />
                <InputField id="last_name" label="Last Name" type="text" placeholder="Enter Last Name"
                    v-model="form.last_name" required />
                <InputField id="email" label="Email" type="email" placeholder="Enter E-mail Address"
                    v-model="form.email" required />
                <InputField id="username" label="Username" type="text" placeholder="Enter Username"
                    v-model="form.username" required />
                <InputField id="password" label="Password" type="password" placeholder="Enter Password"
                    v-model="form.password" required />
                <InputField id="password2" label="Confirm Password" type="password" placeholder="Confirm Password"
                    v-model="form.password2" required />
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
                    up</button>
            </form>
            <div class="text-gray-600">
                <span>Already have an account? </span>
                <router-link class="text-violet-800 font-bold hover:underline" to="/sign-in">Sign in</router-link> to
                your account
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
                first_name: '',
                last_name: '',
                email:'',
                username: '',
                password: '',
                password2:'',
                errors: []
            },
            isSubmitting: false
        };
    },
    methods: {
        async handleSubmit() {
            //console.table(this.form);
            this.form.errors = []

            if (!this.form.errors.length) {
                this.isSubmitting = true;
                const form = {
                    first_name: this.form.first_name,
                    last_name: this.form.last_name,
                    username: this.form.username,
                    email: this.form.email,
                    password: this.form.password,
                };
                try {
                    //console.table(form)
                    const response = await axios.post("/api/v1/users/", form);
                    this.$router.push('/sign-in')

                } catch (error) {
                    if (error.response) {
                        for (const property in error.response.data) {

                            const errors = error.response.data[property];
                            if (Array.isArray(errors)) {
                                errors.forEach(err => this.form.errors.push(err));
                            } else {
                                this.form.errors.push(errors);
                            }
                        }
                    } else {
                        this.form.errors.push('Something went wrong. Please try again later.');
                        console.log(JSON.stringify(error));
                    }
                } finally {
                    this.isSubmitting = false;
                }
            }


            // Handle form submission logic here
        }
    },
    mounted() {
        document.title = 'Sign up | Lets Learn'
    }
}
</script>