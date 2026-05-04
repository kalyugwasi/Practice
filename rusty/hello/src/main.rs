#[cfg(target_pointer_width = "64")]
fn main() {
    println!("64-bit");
}

#[cfg(target_pointer_width = "32")]
fn main() {
    println!("32-bit");
}
