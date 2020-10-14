<template>
  <label>
    <input type="radio" name="dark" checked />
    <span class="design"></span>
    <span class="text">Option 1</span>
  </label>
</template>

<script>
export default {}
</script>

<style lang="scss" scoped>
label {
  --primary: hsl(1, 100%, 68%);
  --other: hsl(0, 0%, 90%);

  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-wrap: nowrap;

  margin: 12px 0;

  cursor: pointer;
  position: relative;
}

input {
  opacity: 0;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  z-index: -1;
}

.design {
  width: 16px;
  height: 16px;

  border: 1px solid var(--other);
  border-radius: 100%;
  margin-right: 16px;

  position: relative;
}

.design::before,
.design::after {
  content: '';
  display: block;

  width: inherit;
  height: inherit;

  border-radius: inherit;

  position: absolute;
  transform: scale(0);
  transform-origin: center center;
}

.design:before {
  background: var(--other);
  opacity: 0;
  transition: 0.3s;
}

.design::after {
  background: var(--primary);
  opacity: 0.4;
  transition: 0.6s;
}

.text {
  color: var(--other);
  font-weight: bold;
}

/* checked state */
input:checked + .design::before {
  opacity: 1;
  transform: scale(0.5);
}

/* other states */
input:hover + .design,
input:focus + .design {
  border: 1px solid var(--primary);
}

input:hover + .design:before,
input:focus + .design:before {
  background: var(--primary);
}

input:hover ~ .text {
  color: var(--primary);
}

input:focus + .design::after,
input:active + .design::after {
  opacity: 0.1;
  transform: scale(2.6);
}
</style>