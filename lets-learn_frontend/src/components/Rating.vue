<template>
    <div class="flex">
        <button v-for="(star, index) in stars" :key="index" @click="setRating(index + 1)"
            @mouseover="hoverRating(index + 1)" @mouseleave="leaveRating" class="focus:outline-none">
            <svg :class="index < currentRating ? 'text-yellow-500' : 'text-gray-300'" class="w-4 h-4"
                fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.286 3.98a1 1 0 00.95.69h4.178c.969 0 1.371 1.24.588 1.81l-3.39 2.48a1 1 0 00-.363 1.118l1.287 3.98c.3.922-.755 1.688-1.54 1.118l-3.39-2.48a1 1 0 00-1.175 0l-3.39 2.48c-.784.57-1.838-.196-1.54-1.118l1.287-3.98a1 1 0 00-.363-1.118l-3.39-2.48c-.783-.57-.38-1.81.588-1.81h4.178a1 1 0 00.95-.69l1.287-3.98z" />
            </svg>
        </button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            currentRating: 0,
            tempRating: 0,
        };
    },
    computed: {
        stars() {
            return Array(5).fill(0);
        },
    },
    methods: {
        setRating(rating) {
            this.currentRating = rating;
        },
        hoverRating(rating) {
            this.tempRating = this.currentRating;
            this.currentRating = rating;
        },
        leaveRating() {
            this.currentRating = this.tempRating;
        },
    },
};
</script>

<style scoped></style>
