<template>
    <div class="mb-3 text-sm">
        <label :for="id" class="block text-violet-800 font-medium mb-2">
            {{ label }}
        </label>
        <input :id="id" :type="type" :placeholder="placeholder" v-model="inputValue" v-bind="$attrs"
            class=" p-2 rounded border border-gray-400 focus:outline-violet-800 w-full block" />
    </div>
</template>

<script>
export default {
    name: 'InputField',
    props: {
        id: {
            type: String,
            required: true
        },
        label: {
            type: String,
            required: true
        },
        type: {
            type: String,
            default: 'text',
            validator: function (value) {
                return ['text', 'number', 'password', 'email', 'file'].includes(value);
            }
        },
        placeholder: {
            type: String,
            default: ''
        },
        modelValue: {
            type: [String, Number],
            default: ''
        }
    },
    data() {
        return {
            inputValue: this.modelValue
        };
    },
    watch: {
        inputValue(newValue) {
            this.$emit('update:modelValue', newValue);
        },
        modelValue(newValue) {
            this.inputValue = newValue;
        }
    }
};
</script>
