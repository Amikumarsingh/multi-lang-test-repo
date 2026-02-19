#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }

    #[test]
    fn test_multiply() {
        assert_eq!(multiply(4, 5), 20);
    }

    #[test]
    fn test_divide() {
        assert_eq!(divide(10.0, 2.0), 5.0);
    }

    #[test]
    fn test_calculate_average() {
        let nums = vec![1, 2, 3, 4, 5];
        assert_eq!(calculate_average(&nums), 3.0);
    }
}
