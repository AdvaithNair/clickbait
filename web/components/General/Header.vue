<template>
    <div>
        <div class="header">
            <div class="content">
                <img src="~/assets/img/logo/icon.svg" class="logo" />
                <h1>clickbait</h1>
            </div>
        </div>
        <div class="under" />
    </div>
</template>

<script>
export default {};
</script>

<style scoped>
.header {
    background: #ef6e26;
    width: 100%;
    height: 65px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.content {
    display: flex;
    justify-content: center;
    align-items: center;
    max-width: 1220px;
    width: 100%;
    padding: 0px 20px;
}

.content h1 {
    color: white;
    font-weight: 500;
    font-size: 40px;
}

.under {
    background: #fbb03b;
    width: 100%;
    height: 5px;
}

.logo {
    height: 45px;
    width: 45px;
    margin-right: 20px;
}
</style>
